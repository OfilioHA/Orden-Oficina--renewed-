import { InputGroup, Button, Form } from "react-bootstrap";
import { InputField } from "./field";
import { useCallback, useState } from "react";

export function PasswordField(props) {

    const [type, setType] = useState("password");

    const handleClickType = useCallback(() => {
        const newType = type == "password" ? "text" : 'password';
        setType(newType);
    }, [type]);

    const labels = {
        password: 'Visualizar',
        text: 'Ocultar'
    }

    return (
        <InputGroup>
            <InputField
                Component={Form.Control}
                type={type}
                {...props}
            />
            <Button
                variant="outline-info"
                type="button"
                onClick={handleClickType}
            >
                {labels[type]}
            </Button>
        </InputGroup>
    )
}


