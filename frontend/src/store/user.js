import { create } from "zustand";

export const useUserStore = create((set) => ({
  user: null,
  updateUser: (user) => set({ user }),
  cleanUser: () => set({ user: null }),
}));
