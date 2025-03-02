import { NavLink } from "react-router";
import { OverlayTrigger, Tooltip, Nav, Button } from "react-bootstrap";

export function SideBar() {
    const items = [
        {
            title: "Home",
            to: "/home",
        },
        {
            title: "Tareas",
            to: "/tasks",
        },
        {
            title: "Cumpleaños",
            to: "/birthdays",
        },
    ];

    return (
        <div
            className="min-vh-100 d-flex flex-column flex-shrink-0 bg-light"
        >
            <Nav
                className="flex-column nav-flush mb-auto"
                variant="pills"
            >
                {items.map(({ to, title }, index) => {
                    return (
                        <Nav.Item key={index}>
                            <Nav.Link
                                as={NavLink}
                                to={to}
                                className="py-3 rounded-0 border-bottom"
                            >
                                {title}
                            </Nav.Link>
                        </Nav.Item>
                    );
                })}
            </Nav>
            <div className="d-grid ">
                <hr className="my-0" />
                <Button
                    variant="link"
                    className="text-decoration-none py-2 text-start"
                >
                    Salir
                </Button>
            </div>
        </div>
    );
}