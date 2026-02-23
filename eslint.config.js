import { defineConfig } from 'eslint/config';
import tslint from 'typescript-eslint';
import ngLint from 'angular-eslint';

export default defineConfig(
  tslint.configs.recommended,
  ngLint.configs.tsRecommended,
  // ...ngLint.configs.templateRecommended,
  // ...ngLint.configs.templateAccessibility,
  {
    ignores: [
      ".angular/",
      "coverage/",
      "dist/",
      "node_modules/",
      "cypress/",
      "cypress.config.ts",
    ]
  },
  {
    files: ['src/**/*.ts'],
    languageOptions: {
      parserOptions: {
        project: ['tsconfig.*?.json'],
        createDefaultProgram: true,
      },
    },
    plugins: {
      'tslint': tslint.plugin,
      'ngLint': ngLint.tsPlugin,
    },
    processor: ngLint.processInlineTemplates,
    rules: {
      'ngLint/directive-selector': [
        'error',
        { type: 'attribute', style: 'camelCase' }
      ],
      'ngLint/component-selector': [
        'error',
        { type: 'element', prefix: 'app', style: 'kebab-case' },
      ],
      'ngLint/prefer-standalone': 0,
      quotes: ['error', 'single', { allowTemplateLiterals: true }],
      'tslint/no-misused-promises': ['error'],
    },
  },
  // {
  //   files: ['src/**/*.html'],
  //   rules: {
  //     'max-len': ['error', { code: 79 }],
  //   },
  // },
);
