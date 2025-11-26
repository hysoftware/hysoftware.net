import { defineConfig } from 'cypress'

export default defineConfig({

  e2e: {
    'baseUrl': 'http://localhost:4200',
    // supportFolder: './cypress/support',
    supportFile: './cypress/support/commands.ts',
  },


  component: {
    devServer: {
      framework: 'angular',
      bundler: 'webpack',
    },
    specPattern: '**/*.cy.ts',
    supportFile: './cypress/support/component.ts',
  }

})
