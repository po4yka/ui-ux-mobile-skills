import ora from 'ora';
import prompts from 'prompts';
import { AI_FOLDERS, AI_TYPES, type AIType, type InstallOptions } from '../types/index.js';
import { detectAIFolders, isSkillInstalled } from '../utils/detect.js';
import { extractAll, extractSkill } from '../utils/extract.js';
import { logger } from '../utils/logger.js';

export async function initCommand(options: Partial<InstallOptions>): Promise<void> {
  const targetDir = process.cwd();

  // If no AI type specified, prompt user
  let aiType = options.ai;
  if (!aiType) {
    const detected = detectAIFolders(targetDir);

    if (detected.length > 0) {
      logger.info(`Detected AI folders: ${detected.join(', ')}`);
    }

    const response = await prompts({
      type: 'select',
      name: 'ai',
      message: 'Which AI assistant do you want to install the skill for?',
      choices: AI_TYPES.map((t) => ({ title: t, value: t })),
      initial: detected.length === 1 ? AI_TYPES.indexOf(detected[0]) : AI_TYPES.indexOf('all'),
    });

    if (!response.ai) {
      logger.error('Installation cancelled.');
      process.exit(1);
    }

    aiType = response.ai as AIType;
  }

  const spinner = ora('Installing UI/UX Mobile skill...').start();

  try {
    if (aiType === 'all') {
      // Check for existing installations
      for (const ai of Object.keys(AI_FOLDERS) as Array<Exclude<AIType, 'all'>>) {
        if (isSkillInstalled(targetDir, ai) && !options.force) {
          spinner.fail(`Skill already installed for ${ai}. Use --force to overwrite.`);
          process.exit(1);
        }
      }

      extractAll(targetDir, options.force);
      spinner.succeed('UI/UX Mobile skill installed for Claude and Codex.');
    } else {
      if (isSkillInstalled(targetDir, aiType) && !options.force) {
        spinner.fail(`Skill already installed for ${aiType}. Use --force to overwrite.`);
        process.exit(1);
      }

      extractSkill(targetDir, aiType, options.force);
      spinner.succeed(`UI/UX Mobile skill installed for ${aiType}.`);
    }

    logger.info('');
    logger.success('Installation complete!');
    logger.info('');
    logger.step('Test the skill with:');

    if (aiType === 'all' || aiType === 'claude') {
      console.log(`  python3 .claude/skills/ui-ux-mobile/scripts/search.py "button" --domain component`);
    }
    if (aiType === 'all' || aiType === 'codex') {
      console.log(`  python3 .codex/skills/ui-ux-mobile/scripts/search.py "button" --domain component`);
    }
  } catch (error) {
    spinner.fail('Installation failed.');
    logger.error(error instanceof Error ? error.message : String(error));
    process.exit(1);
  }
}
