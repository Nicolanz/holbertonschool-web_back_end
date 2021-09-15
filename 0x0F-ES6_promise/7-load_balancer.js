export default function loadBalancer(chinaDownload, USDownload) {
  const val = Promise.race([chinaDownload, USDownload]);
  return val;
}
