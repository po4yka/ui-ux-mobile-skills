#!/usr/bin/env node
import { program } from 'commander';
import { AI_TYPES, type AIType } from './types/index.js';
import { initCommand } from './commands/init.js';
import { updateCommand } from './commands/update.js';
import { versionsCommand } from './commands/versions.js';
import { logger } from './utils/logger.js';

function parseAIOption(value: unknown): AIType | undefined {
  if (value === undefined || value === null) {
    return undefined;
  }
  if (typeof value !== 'string' || !AI_TYPES.includes(value as AIType)) {
    const readable = typeof value === 'string' ? value : JSON.stringify(value);
    logger.error(`Invalid --ai value: ${readable}`);
    logger.info(`Valid values: ${AI_TYPES.join(', ')}`);
    logger.info('Example: uipro-mobile init --ai codex');
    process.exit(1);
  }
  return value as AIType;
}

program
  .name('uipro-mobile')
  .description('CLI tool for installing UI/UX Mobile skill for Claude Code and OpenAI Codex')
  .version('1.0.0');

program
  .command('init')
  .description('Install UI/UX Mobile skill in the current directory')
  .option('-a, --ai <type>', `AI assistant type (${AI_TYPES.join(', ')})`)
  .option('-f, --force', 'Overwrite existing installation')
  .action(async (options) => {
    await initCommand({
      ai: parseAIOption(options.ai),
      force: options.force,
    });
  });

program
  .command('update')
  .description('Update UI/UX Mobile skill to the latest version')
  .option('-a, --ai <type>', `AI assistant type (${AI_TYPES.join(', ')})`)
  .action(async (options) => {
    await updateCommand({
      ai: parseAIOption(options.ai),
    });
  });

program
  .command('versions')
  .description('List available versions')
  .action(() => {
    versionsCommand();
  });

program.parse();
