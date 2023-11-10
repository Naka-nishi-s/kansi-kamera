import { atom } from "recoil";

type AuthState = {
  isLoggedIn: boolean;
};

export const authState = atom<AuthState>({
  key: "authState",
  default: {
    isLoggedIn: false,
  },
});
