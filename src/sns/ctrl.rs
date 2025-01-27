use ::dioxus::prelude::*;

use crate::fontawesome::{GITHUB, GITLAB, KEYBASE};
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
          Some(GITHUB.to_string()),
          "https://github.com/hiroaki-yamamoto",
          "Github",
        ),
        Link::new(
          Some(GITLAB.to_string()),
          "https://gitlab.com/hiroaki-yamamoto",
          "Gitlab",
        ),
        Link::new(
          Some(KEYBASE.to_string()),
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
