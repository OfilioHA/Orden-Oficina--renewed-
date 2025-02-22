import { Field } from "formik";

export function InputField({ Component, ...props }) {
    return (
        <Field {...props}>
            {({ field, form, meta, ...rest }) => {

                const isValid = meta.touched && !form.errors[field.name];
                const isInvalid = meta.touched && !isValid;

                return (
                    <Component
                        isValid={isValid}
                        isInvalid={isInvalid}
                        {...field}
                        {...props}
                        {...rest}
                    />
                )
            }}
        </Field>
    );
}