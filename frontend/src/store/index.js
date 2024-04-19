import { createStore } from "vuex";
import todoModule from "./todo";

const store = createStore({
  modules: {
    todo: todoModule,
  },
  state() {
    return {};
  },
  mutations: {},
  getters: {},
  actions: {},
});

export default store;
