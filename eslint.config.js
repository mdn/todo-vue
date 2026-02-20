import js from "@eslint/js";
import pluginVue from "eslint-plugin-vue";
import skipFormatting from "@vue/eslint-config-prettier/skip-formatting";
import globals from "globals";

export default [
  { ignores: ["dist/"] },
  js.configs.recommended,
  ...pluginVue.configs["flat/essential"],
  skipFormatting,
  { languageOptions: { globals: globals.browser } },
];
