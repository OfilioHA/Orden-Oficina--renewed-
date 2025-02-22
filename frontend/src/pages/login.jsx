import { Container, Row, Col } from 'react-bootstrap';
import { LoginForm } from '../components/login/form';

export function LoginPage() {
    return (
        <Container fluid>
            <Row className="align-items-md-center justify-content-between">
                <Col md="6" className='min-vh-100 bg-success'>
                </Col>
                <Col md="6">
                    <Row className='min-vh-100 justify-content-center align-items-center'>
                        <Col md={8}>
                            <LoginForm />
                        </Col>
                    </Row>
                </Col>
            </Row>
        </Container>
    );
}