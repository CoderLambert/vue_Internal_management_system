const publicPath = process.env.NODE_ENV === 'production' ? '/static/' : '/'

module.exports = {
  publicPath,

  configureWebpack: {
    plugins: []
  },

  css: {
    extract: false
  }

}
