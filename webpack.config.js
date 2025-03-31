import path from "path";
import BundleTracker from "webpack-bundle-tracker";
import TerserPlugin from "terser-webpack-plugin";

const __dirname = path.dirname('.');

export default {
  entry: {
    script: './base_static/global/js/script.js', 
    homeTeachers: './base_static/global/js/teachersHome.js', 
    validation: './base_static/global/js/validation.js', 
    codeVerify: './base_static/global/js/codeVerify.js', 
  },
  output: {
    path: path.resolve(__dirname, "base_static/build/"),
    filename: "[name].bundle.js",
  },
  module: {
    rules: [
      {
        test: /\.js$/, // Processar arquivos JS com Babel
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
          options: {
            presets: ["@babel/preset-env"],
          },
        },
      },
      {
        test: /\.css$/, // Processar arquivos CSS
        use: ["style-loader", "css-loader"],
      },
    ],
  },
  plugins: [
    new BundleTracker({ filename: path.join(__dirname, "webpack-stats.json") }),

  ],
  mode: "production",
};
