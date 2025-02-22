import { useCallback } from 'react';
import { Button, Card, Form } from 'react-bootstrap';
import { FormikProvider, useFormik } from 'formik';
import * as Yup from 'yup';
import { useFetch } from '@/hooks/useFetch';
import { InputField } from '@/components/utils/inputs/field';
import { PasswordField } from '@/components/utils/inputs/password';

export function LoginForm() {

    const fetcher = useFetch();

    const initialValues = {
        username: '',
        password: '',
        remember: false
    }

    const validationSchema = Yup.object({
        username: Yup.string().required(),
        password: Yup.string().required(),
        remember: Yup.boolean().required(),
    });

    const handleSubmit = useCallback(async (values) => {
        const { data, status } = await fetcher.makeRequest('/auth/login', {
            method: 'POST',
            data: values
        });
        if (status != 200) return;
        const { token, user } = data;

    }, []);

    const formik = useFormik({ initialValues, validationSchema, onSubmit: handleSubmit });

    return (
        <Card className='shadow'>
            <FormikProvider value={formik}>
                <Form onSubmit={formik.handleSubmit} noValidate>
                    <Card.Body>
                        <Card.Title>
                            Login
                        </Card.Title>
                        <hr />

                        <Form.Group controlId='username' className='mb-3'>
                            <Form.Label>
                                Usuario
                            </Form.Label>
                            <InputField
                                Component={Form.Control}
                                name='username'
                            />
                        </Form.Group>

                        <Form.Group controlId='password' className='mb-3'>
                            <Form.Label>
                                Contrasena
                            </Form.Label>
                            <PasswordField name='password' />
                        </Form.Group>

                        <Form.Group>
                            <InputField
                                Component={Form.Check}
                                name="remember"
                                label="Remember me"
                                id="remember"
                                isValid={false}
                            />
                        </Form.Group>

                    </Card.Body>
                    <Card.Footer>
                        <div className="d-flex justify-content-end">
                            <Button variant='primary' type='submit'>
                                Ingresar
                            </Button>
                        </div>
                    </Card.Footer>
                </Form>
            </FormikProvider>
        </Card>
    )
}