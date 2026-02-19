import js from "@eslint/js";
import pluginVue from "eslint-plugin-vue";
import skipFormatting from "@vue/eslint-config-prettier/skip-formatting";

export default [
  { ignores: ["dist/"] },
  js.configs.recommended,
  ...pluginVue.configs["flat/essential"],
  skipFormatting,
];
