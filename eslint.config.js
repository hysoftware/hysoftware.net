import tslint from 'typescript-eslint';
import ngLint from 'angular-eslint';

const tsLintConfig = {
  files: ['src/**/*.ts'],
  languageOptions: {
    parserOptions: {
      project: ['tsconfig.*?.json'],
      createDefaultProgram: true,
    },
    parser: tslint.parser,
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
};

// const htmlConfig = {
//   files: ['src/**/*.html'],
//   plugins: ngLint.templatePlugin,
//   languageOptions: {
//     parser: ngLint.templateParser,
//   },
//   rules: {
//     'max-len': ['error', { code: 79 }],
//   },
// };

const exclude = {
  ignores: [
    ".angular/",
    "coverage/",
    "dist/",
    "node_modules/",
    "cypress/",
    "cypress.config.ts",
  ]
};

export default [
  tsLintConfig, exclude,
];
