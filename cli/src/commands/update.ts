import ora from 'ora';
import prompts from 'prompts';
import { AI_FOLDERS, AI_TYPES, type AIType, type UpdateOptions } from '../types/index.js';
import { detectAIFolders, isSkillInstalled } from '../utils/detect.js';
import { extractAll, extractSkill } from '../utils/extract.js';
import { logger } from '../utils/logger.js';

export async function updateCommand(options: Partial<UpdateOptions>): Promise<void> {
  const targetDir = process.cwd();

  // If no AI type specified, detect and prompt
  let aiType = options.ai;
  if (!aiType) {
    const detected = detectAIFolders(targetDir);
    const installed: Array<Exclude<AIType, 'all'>> = [];

    for (const ai of detected as Array<Exclude<AIType, 'all'>>) {
      if (isSkillInstalled(targetDir, ai)) {
        installed.push(ai);
      }
    }

    if (installed.length === 0) {
      logger.error('No UI/UX Mobile skill installation found. Run "uipro-mobile init" first.');
      process.exit(1);
    }

    if (installed.length === 1) {
      aiType = installed[0];
      logger.info(`Found installation for ${aiType}.`);
    } else {
      const response = await prompts({
        type: 'select',
        name: 'ai',
        message: 'Which installation do you want to update?',
        choices: [...installed.map((t) => ({ title: t, value: t })), { title: 'all', value: 'all' }],
      });

      if (!response.ai) {
        logger.error('Update cancelled.');
        process.exit(1);
      }

      aiType = response.ai as AIType;
    }
  }

  const spinner = ora('Updating UI/UX Mobile skill...').start();

  try {
    if (aiType === 'all') {
      extractAll(targetDir, true);
      spinner.succeed('UI/UX Mobile skill updated for all installations.');
    } else {
      if (!isSkillInstalled(targetDir, aiType)) {
        spinner.fail(`No ${aiType} installation found. Run "uipro-mobile init --ai ${aiType}" first.`);
        process.exit(1);
      }

      extractSkill(targetDir, aiType, true);
      spinner.succeed(`UI/UX Mobile skill updated for ${aiType}.`);
    }

    logger.success('Update complete!');
  } catch (error) {
    spinner.fail('Update failed.');
    logger.error(error instanceof Error ? error.message : String(error));
    process.exit(1);
  }
}
