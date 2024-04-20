export default {
  namespaced: true,
  state() {
    return {
      items: [],
    };
  },
  mutations: {
    initialItems(state, items) {
      state.items = items;
    },
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
    findItemById: (state) => (id) => {
      return state.items.find((item) => item.id === id);
    },
  },
  actions: {
    async initialItems(context) {
      const response = await fetch("http://127.0.0.1:8000/todo/");
      if (response.ok) {
        const items = await response.json();
        context.commit("initialItems", items);
      }
    },
    async addItem(context, payload) {
      const response = await fetch("http://127.0.0.1:8000/todo/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          label: payload.toDoLabel,
        }),
      });
      if (response.ok) {
        const item = await response.json();
        context.commit("addItem", item);
      }
    },
    async editItem(context, payload) {
      if (payload.type === "status") {
        const item = context.getters["findItemById"](payload.itemId);
        const response = await fetch(`http://127.0.0.1:8000/todo/${item.id}`, {
          method: "PATCH",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            done: !item.done,
          }),
        });
        if (response.ok) {
          context.commit("toggleDoneStatus", item.id);
        }
      } else if (payload.type === "label") {
        const response = await fetch(
          `http://127.0.0.1:8000/todo/${payload.itemId}`,
          {
            method: "PATCH",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              label: payload.newLabel,
            }),
          }
        );
        if (response.ok) {
          context.commit("editItemLabel", {
            id: payload.itemId,
            label: payload.newLabel,
          });
        }
      }
    },
    async deleteItem(context, payload) {
      const response = await fetch(
        `http://127.0.0.1:8000/todo/${payload.itemId}`,
        {
          method: "DELETE",
        }
      );
      if (response.ok) {
        context.commit("deleteItem", payload.itemId);
      }
    },
  },
};
