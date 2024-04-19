import uniqueId from "lodash.uniqueid";

export default {
  namespaced: true,
  state() {
    return {
      items: [
        { id: uniqueId(), label: "Learn Vue", done: false },
        {
          id: uniqueId(),
          label: "Create a Vue project with the CLI",
          done: true,
        },
        { id: uniqueId(), label: "Create a to-do list", done: false },
      ],
    };
  },
  mutations: {
    addItem(state, item) {
      state.items.push(item);
    },
    toggleDoneStatus(state, id) {
      const todo = state.items.find((item) => item.id === id);
      todo.done = !todo.done;
    },
    editItemLabel(state, payload) {
      const todo = state.items.find((item) => item.id === payload.id);
      todo.label = payload.label;
    },
    deleteItem(state, id) {
      const itemIndex = state.items.findIndex((item) => item.id === id);
      state.items.splice(itemIndex, 1);
    },
  },
  getters: {
    items(state) {
      return state.items;
    },
    totalItems(state) {
      return state.items.length;
    },
    totalDoneItems(state) {
      return state.items.filter((item) => item.done).length;
    },
  },
  actions: {
    addItem(context, payload) {
      const id = uniqueId();
      const label = payload.toDoLabel;
      const done = false;
      context.commit("addItem", { id, label, done });
    },
    editItem(context, payload) {
      if (payload.type === "status") {
        context.commit("toggleDoneStatus", payload.id);
      } else if (payload.type === "label") {
        context.commit("editItemLabel", {
          id: payload.id,
          label: payload.newLabel,
        });
      }
    },
    deleteItem(context, payload) {
      context.commit("deleteItem", payload.id);
    },
  },
};
