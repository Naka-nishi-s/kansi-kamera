import { defineConfig } from 'vite';

export default defineConfig({
  build: {
    outDir:"../kanshiKamera/static/",
    emptyOutDir:true,
    rollupOptions: {
      output: {
        entryFileNames: `assets/bundle.js`, // エントリポイントのJSファイル名
        chunkFileNames: `assets/[name].js`, // 非同期にロードされるチャンクファイル名
        assetFileNames: ({name}) => {
          if (/\.(css|scss|sass)$/.test(name)) {
            return 'assets/styles.css'; // CSSファイル名
          }
          return 'assets/[name].[ext]'; // その他のアセットファイル名
        }
      }
    }
  }
})