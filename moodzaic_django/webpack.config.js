
var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  context: __dirname,
  entry: './frontend/src/index.js',
  output: {
    path: path.resolve('./frontend/bundles/'),
    filename: "[name]-[hash].js",
  },
  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
  ],

  module: {

    rules: [
      {test: /\.js$/, exclude: /node_modules/, use: ['babel-loader']},
      {
        test: /\.css$/,
        use: [
          'style-loader',
          'css-loader'
        ],
      },
      {test: /\.(png|svg|jpg|gif)$/, use: ['file-loader']},

    ],
  },
  resolve: {
    extensions: ['*', '.js', '.jsx']
  }
};
