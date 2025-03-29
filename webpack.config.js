import path from "path";
import { fileURLToPath } from "url";
import BundleTracker from "webpack-bundle-tracker";

const __dirname = path.dirname('.');

export default {
  entry: {
    script: './base_static/global/js/script.js', 
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
  mode: "development",
};
