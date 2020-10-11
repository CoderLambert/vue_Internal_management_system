const publicPath = process.env.NODE_ENV === 'production' ? '/static/' : '/'
const CompressionWebpackPlugin = require("compression-webpack-plugin");


module.exports = {
  publicPath,
  productionSourceMap: false,
  configureWebpack: {
    plugins: [
      new CompressionWebpackPlugin({
        filename: '[path].gz[query]',
        algorithm: 'gzip',
        test: new RegExp('\\.(js)$'),
        threshold: 1024
        // minRatio: 0.8,
        // deleteOriginalAssets: true
      })
    ]
  },

  css: {
    extract: false
  }

}
