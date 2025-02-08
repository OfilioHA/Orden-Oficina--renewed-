import { Suspense } from "react";
import { Outlet } from "react-router";

export function CleanLayout() {
  return (
    <div id="clean-layout">
      <main>
        <Suspense>
          <Outlet />
        </Suspense>
      </main>
    </div>
  );
}
