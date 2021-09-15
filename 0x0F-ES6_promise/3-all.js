import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const upPicture = uploadPhoto();
  const createUs = createUser();

  upPicture
    .then((event) => { process.stdout.write(`${event.body} `); })
    .catch(() => { console.log('Signup system offline'); });

  createUs
    .then((res) => { console.log(res.firstName, res.lastName); })
    .catch(() => { console.log('Signup system offline'); });
}
