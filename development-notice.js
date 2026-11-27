// Acknowledge once per browser tab session; never require payment.
(() => {
  const dialog = document.getElementById('development-notice');
  const ack = document.getElementById('development-ack');
  const key = 'viseu-development-notice-v1';
  let acknowledged = false;
  try { acknowledged = sessionStorage.getItem(key) === 'read'; } catch {}
  if (acknowledged) return;
  dialog.addEventListener('cancel', event => event.preventDefault());
  ack.addEventListener('click', () => {
    try { sessionStorage.setItem(key, 'read'); } catch {}
    dialog.close();
    document.getElementById('app').focus({preventScroll:true});
  });
  dialog.showModal();
})();
