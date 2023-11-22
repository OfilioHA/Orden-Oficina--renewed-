/** @type {import('./$types').PageLoad} */
export async function load({ params }) {
  return {
    post: {
      title: `Title for goes here`,
      content: `Content for goes here`,
    },
  };
}
