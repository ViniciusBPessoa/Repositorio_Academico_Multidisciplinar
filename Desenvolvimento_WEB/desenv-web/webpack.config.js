const { DefinePlugin } = require('webpack');
const packageJson = require('./package.json');

const buildInfo = {
  package: {
    version: JSON.stringify(packageJson.version),
    name: JSON.stringify(packageJson.author.name),
    email: JSON.stringify(packageJson.author.email),
    url: JSON.stringify(packageJson.author.url),
  },
};

module.exports = {
  devtool:  'source-map',
  target: 'node',
  plugins: [
    new DefinePlugin({ _BUILD_INFO_: buildInfo }),
  ],
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: [
          {
            loader: 'ts-loader',
            options: {
              transpileOnly: true,
            },
          },
        ],
        exclude: [
          /node_modules/,
          /dist/,
          /\.spec\.tsx?$/, 
        ],
      },
    ],
  },
};
