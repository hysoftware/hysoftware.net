use crate::links::Link;

#[derive(Debug)]
pub struct Ctrl {
  links: Vec<Link>,
}

impl Ctrl {
  pub fn new() -> Self {
    Self {
      links: vec![
        Link::new(
          "fa-brands fa-github".into(),
          "https://github.com/hiroaki-yamamoto",
          "Github",
        ),
        Link::new(
          "fa-brands fa-github".into(),
          "https://gitlab.com/hiroaki-yamamoto",
          "Gitlab",
        ),
        Link::new(
          "fa-brands fa-keybase".into(),
          "https://keybase.io/hyamamoto",
          "Keybase",
        ),
      ],
    }
  }
  pub fn links(&self) -> &Vec<Link> {
    return &self.links;
  }
}
