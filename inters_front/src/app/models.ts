export interface District {
  id: number;
  name: string;
}
  
export interface AuthToken {
  token: string;
}
export interface Product {
  id: number;
  streets: string;
  price: number;
  description: string;
  image: string;
  link: string;
  rating : number;
  district : string;
}
// export interface Districts {
//   id: number;
//   district_name: string;
//   image: string;
// }