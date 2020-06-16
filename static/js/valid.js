function validateForm() {
  var names = ['name', 'email', 'message'];
  var errorCount = 0;
  names.forEach(function(el) {
    var val = document.forms["query_m"][el].value;
    if (val == null || val == "") {
      document.getElementById(el + '_error').textContent = el.toUpperCase().replace('_', ' ') + " must be filled out";
      ++errorCount;
    }
  });
  if (errorCount) return false;
}
