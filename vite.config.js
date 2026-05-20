import { defineConfig } from "vite"
import { resolve } from "path"
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  base: "/static/",
  plugins: [
    tailwindcss(),
  ],
  resolve: {
    alias: {
        "@": resolve("./static"),
    },
  },
  build: {
    manifest: "manifest.json",
    outDir: resolve("./assets"),
    rollupOptions: {
      input: {
        main: "static/js/main.js"
      }
    }
  }
})