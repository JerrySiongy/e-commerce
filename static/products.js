const products = [
  {
    id: 0,
    name: "T-shirt 1",
    price: 29.99,
    instock: 100,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shirts/t1.png",
  },
  {
    id: 1,
    name: "T-shirt 2",
    price: 24.99,
    instock: 43,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shirts/t2.png",
  },
  {
    id: 2,
    name: "T-shirt 3",
    price: 19.99,
    instock: 10,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shirts/t3.png",
  },
  {
    id: 3,
    name: "T-shirt 4",
    price: 25.99,
    instock: 5,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shirts/t4.png",
  },
  {
    id: 4,
    name: "T-shirt 5",
    price: 29.99,
    instock: 4,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shirts/t5.png",
  },
  {
    id: 5,
    name: "T-shirt 6",
    price: 39.99,
    instock: 40,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shirts/t6.png",
  },
];

const shoes = [
  {
    id: 0,
    name: "adizero",
    price: 3500,
    instock: 100,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shoes/adizero.jpeg",
  },
  {
    id: 0,
    name: "airmax 97",
    price: 3500,
    instock: 100,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shoes/air_max_97.jpeg",
  },
  {
    id: 0,
    name: "airmax 95",
    price: 3500,
    instock: 100,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shoes/air_max_95.jpeg",
  },
  {
    id: 0,
    name: "airmax tn",
    price: 3500,
    instock: 100,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shoes/airmax_tn.jpeg",
  },
  {
    id: 0,
    name: "airforce 1 custome",
    price: 3500,
    instock: 100,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shoes/airforce_1_custome.jpeg",
  },
  {
    id: 0,
    name: "airforce 1",
    price: 3500,
    instock: 100,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shoes/airforce_1.jpeg",
  },
  {
    id: 0,
    name: "airmax dn",
    price: 3500,
    instock: 100,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shoes/airmax_dn.jpeg",
  },
  {
    id: 0,
    name: "cat boots",
    price: 3500,
    instock: 100,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shoes/cat_boots.jpeg",
  },
  {
    id: 0,
    name: "cloud swift k-tech",
    price: 3500,
    instock: 100,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shoes/cloud_swift_k-tech.jpeg",
  },
  {
    id: 0,
    name: "dg",
    price: 3500,
    instock: 100,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shoes/dg.jpeg",
  },
  {
    id: 0,
    name: "dior homie",
    price: 3500,
    instock: 100,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shoes/dior_homie.jpeg",
  },
  {
    id: 0,
    name: "dr martin",
    price: 3500,
    instock: 100,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shoes/dr_martin.jpeg",
  },
  {
    id: 0,
    name: "dr martins boot",
    price: 3500,
    instock: 100,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shoes/dr_martins_boot.jpeg",
  },
  {
    id: 0,
    name: "J5",
    price: 3500,
    instock: 100,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shoes/j5.jpeg",
  },
  {
    id: 0,
    name: "jordan3",
    price: 3500,
    instock: 100,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shoes/jordan3.jpeg",
  },
  {
    id: 0,
    name: "keens opens",
    price: 3500,
    instock: 100,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shoes/keens_opens.jpeg",
  },
  {
    id: 0,
    name: "lv boots",
    price: 3500,
    instock: 100,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shoes/lv_boots.jpeg",
  },
  {
    id: 0,
    name: "new balance 530",
    price: 3500,
    instock: 100,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shoes/new_balance_530.jpeg",
  },
  {
    id: 0,
    name: "new balance1000",
    price: 3500,
    instock: 100,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shoes/new_balance1000.jpeg",
  },
  {
    id: 0,
    name: "Nike sb",
    price: 3500,
    instock: 100,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shoes/nike_sb.jpeg",
  },
  {
    id: 0,
    name: "nocta glide",
    price: 3500,
    instock: 100,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shoes/nocta_glide.jpeg",
  },
  {
    id: 0,
    name: "north face boot",
    price: 3500,
    instock: 100,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shoes/north_face_boot.jpeg",
  },
  {
    id: 0,
    name: "numeris",
    price: 3500,
    instock: 100,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shoes/numeris.jpeg",
  },
  {
    id: 0,
    name: "puma speedcat",
    price: 3500,
    instock: 100,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shoes/puma_speedcat.jpeg",
  },
  {
    id: 0,
    name: "puma suede",
    price: 3500,
    instock: 100,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shoes/puma_suede.jpeg",
  },
  {
    id: 0,
    name: "samba",
    price: 3500,
    instock: 100,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shoes/samba.jpeg",
  },
  {
    id: 0,
    name: "shocks",
    price: 3500,
    instock: 100,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shoes/shocks.jpeg",
  },
  {
    id: 0,
    name: "spot qc",
    price: 3500,
    instock: 100,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shoes/spot_qc.jpeg",
  },
  {
    id: 0,
    name: "vans knu",
    price: 3500,
    instock: 100,
    description:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores, error.",
    imgSrc: "static/images/shoes/vans_knu.jpeg",
  }
];
