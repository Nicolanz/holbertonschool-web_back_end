import { uploadPhoto, createUser } from './utils';
export default async function asyncUploadUser() {
  const photo = uploadPhoto();
  const user = createUser();
  
  return {}
}
