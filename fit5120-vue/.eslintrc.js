module.exports = {
  root: true,
  env: {
    browser: true,
    es2021: true,
    node: true
  },
  extends: [
    'eslint:recommended',
    'plugin:vue/essential' 
  ],
  parserOptions: {
    ecmaVersion: 2021,
    sourceType: 'module'
  },
  rules: {
    'quotes': 'off',
    'semi': 'off',
    'vue/no-multiple-template-root': 'off',
    'no-unused-vars': 'warn',
    'no-console': 'off'
  }
}
