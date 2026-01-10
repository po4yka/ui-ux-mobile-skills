import chalk from 'chalk';

export const logger = {
  info: (msg: string) => console.log(chalk.blue('INFO'), msg),
  success: (msg: string) => console.log(chalk.green('OK'), msg),
  warn: (msg: string) => console.warn(chalk.yellow('WARN'), msg),
  error: (msg: string) => console.error(chalk.red('ERROR'), msg),
  step: (msg: string) => console.log(chalk.cyan('-->'), msg),
};
