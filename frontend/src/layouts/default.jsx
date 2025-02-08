import { Outlet } from "react-router";


export function DefaultLayout() {
  return (
    <div id="layout-default">
      <main>
        <Outlet />
      </main>
    </div>
  );
}
