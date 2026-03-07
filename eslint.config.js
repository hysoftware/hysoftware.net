import tslint from 'typescript-eslint';
import ngLint from 'angular-eslint';

const esLintConfig = {
  files: ['eslint.config.js', 'src/**/*.js'],
  rules: {
    'max-len': ['error', { code: 79 }],
    quotes: ['error', 'single', { allowTemplateLiterals: true }],
    semi: ['error', 'always'],
  },
};

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
    tslint: tslint.plugin,
    ngLint: ngLint.tsPlugin,
    tmpLint: ngLint.templatePlugin,
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
    'tslint/no-misused-promises': ['error'],
    'max-len': ['error', { code: 79, ignoreUrls: true }],
    quotes: ['error', 'single', { allowTemplateLiterals: true }],
    semi: ['error', 'always'],
  },
};

const htmlConfig = {
  files: ['src/app/**/*.html'],
  plugins: ngLint.templatePlugin,
  languageOptions: {
    parser: ngLint.templateParser,
  },
  rules: {
    'max-len': ['error', { code: 79 }],
  },
};

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
  tsLintConfig, htmlConfig, exclude,
];
