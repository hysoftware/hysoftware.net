module.exports = {
  overrides: [
    {
      files: ['*.ts',],
      parserOptions: {
        project: ['tsconfig.*?.json'],
        createDefaultProgram: true
      },
      extends: [
        'plugin:@typescript-eslint/recommended',
        'plugin:@angular-eslint/recommended',
      ],
      rules: {
        '@angular-eslint/directive-selector': [
          'error',
          { type: 'attribute', style: 'camelCase' },
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
    {
      files: ['*.component.html'],
      extends: ['plugin:@angular-eslint/template/recommended'],
      rules: {
        'max-len': ['error', { code: 79 }],
      },
    },
    {
      files: ['*.component.ts'],
      extends: ['plugin:@angular-eslint/template/process-inline-templates'],
    },
  ],
};

// module.exports = {
//   overrides: [
//     {
//       files: ['*.ts'],
//       parserOptions: {
//         project: ['./tsconfig.json', './tsconfig.**.json'],
//       },
//       extends: [
//         'plugin:@typescript-eslint/recommended',
//         'plugin:@angular-eslint/recommended'
//       ],
//       rules: {
//         '@angular-eslint/directive-selector': [
//           'error',
//           { type: 'attribute', prefix: 'app', style: 'camelCase' },
//         ],
//         '@angular-eslint/component-selector': [
//           'error',
//           { type: 'element', prefix: 'app', style: 'kebab-case' },
//         ],
//         quotes: ['error', 'single', { allowTemplateLiterals: true }],
//         '@typescript-eslint/no-misused-promises': ['error'],
//       },
//     },
//     {
//       files: ['*.component.html'],
//       extends: ['plugin:@angular-eslint/template/recommended'],
//       rules: {
//         'max-len': ['error', { code: 79 }],
//       },
//     },
//     {
//       files: ['*.component.ts'],
//       extends: ['plugin:@angular-eslint/template/process-inline-templates'],
//     },
//   ],
// };
