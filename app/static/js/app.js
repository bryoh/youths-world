const basketbtn = document.getElementById('btn-add-to-basket');
const select = document.getElementById('variant-select');

basketbtn.addEventListener("click", (e) => {
  e.preventDefault();
  const variant_id = select.options[select.selectedIndex].value;
  longclawclient.basketList.post({
    prefix: "{% longclaw_api_url_prefix %}",
    data: { variant_id }
  });
});

