module.exports = {
    root: true,
    env: {
        node: true
    },
    'extends': [
        'plugin:vue/essential',
        '@vue/standard'
    ],
    rules: {
        'no-console': process.env.NODE_ENV === 'production' ? 'off' : 'off',
        'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
        'no-trailing-spaces': 'off',
        'space-in-parens': 'off',
        'func-call-spacing': 'off',
        'indent': 'off',
        'space-before-blocks': 'off',
        'camelcase': 'off',
        'eol-last': 'off'
            // 'no-unused-vars':process.env.NODE_ENV === 'production' ? 'error' : 'off'
    },
    parserOptions: {
        parser: 'babel-eslint'
    }
}