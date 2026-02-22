import { defineConfig } from 'eslint/config';
import tslintPlugin from 'typescript-eslint';
import angularESLintPlugin from 'angular-eslint';

export default defineConfig([
  {
    "ignores": [
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
    extends: [
      ...tslintPlugin.configs.recommended,
      ...angularESLintPlugin.configs.tsRecommended,
    ],
    processor: angularESLintPlugin.processInlineTemplates,
    rules: {
      '@angular-eslint/directive-selector': [
        'error',
        { type: 'attribute', style: 'camelCase' }
      ],
      '@angular-eslint/component-selector': [
        'error',
        { type: 'element', prefix: 'app', style: 'kebab-case' },
      ],
      '@angular-eslint/prefer-standalone': 0,
      quotes: ['error', 'single', { allowTemplateLiterals: true }],
      '@typescript-eslint/no-misused-promises': ['error'],
    },
  },
  // {
  //   files: ['src/**/*.html'],
  //   extends: [
  //     ...angularESLintPlugin.configs.templateRecommended,
  //     ...angularESLintPlugin.configs.templateAccessibility,
  //   ],
  //   rules: {
  //     'max-len': ['error', { code: 79 }],
  //   },
  // },

  // {
  //   files: ['src/**/*.component.ts'],
  //   extends: [
  //     ...angularESLintPlugin.configs.templateRecommended,
  //     ...angularESLintPlugin.configs.templateAccessibility,
  //   ],
  // },
]);
