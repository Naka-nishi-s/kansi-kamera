import { Navigate } from "react-router-dom";
import { useRecoilValue } from "recoil";
import { authState } from "./atoms/authState";

type ProtectedRouteProps = {
  children: React.ReactNode;
};

export const AuthCheck: React.FC<ProtectedRouteProps> = ({ children }) => {
  const auth = useRecoilValue(authState);

  if (!auth.isLoggedIn) {
    return <Navigate to="/login" />;
  }

  return <>{children}</>;
};
