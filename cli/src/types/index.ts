export type AIType = 'claude' | 'codex' | 'all';

export const AI_TYPES: AIType[] = ['claude', 'codex', 'all'];

export const AI_FOLDERS: Record<Exclude<AIType, 'all'>, string> = {
  claude: '.claude',
  codex: '.codex',
};

export const AI_SKILL_PATH = 'skills/ui-ux-mobile';

export interface InstallOptions {
  ai: AIType;
  force?: boolean;
}

export interface UpdateOptions {
  ai: AIType;
}

export interface VersionInfo {
  version: string;
  date: string;
  changes: string[];
}
