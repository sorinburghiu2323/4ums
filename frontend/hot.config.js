module.exports = {
  outputDir: './build/static/vue/',
  indexPath: '../../templates/index.html',
  pages: {
    index: 'src/main.js',
  },
  devServer: {
    proxy: 'http://localhost:8000',
    disableHostCheck: true,
  },
};
