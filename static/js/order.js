
$('#phone').inputmask({
    mask: '+7 (9##) ###-##-##',
    definitions: {'#': { validator: "[0-9]", cardinality: 1}},
})

$('#email').inputmask({
    alias: 'email'
})

console.log('script loaded');