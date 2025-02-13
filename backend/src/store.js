import { createStore } from 'vuex'
import {getUser} from "@/api.js"
// Create a new store instance.
export default   createStore({
  state () {
    return {
      user: 0
    }
  },
  mutations: {
    getUser (state,user) {
      state.user = user
    }
  },
    actions: {
        async getUser(context) {
            context.commit('getUser',await getUser())
    }
  }
})
