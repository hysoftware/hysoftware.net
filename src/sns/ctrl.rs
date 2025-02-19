use crate::icon::Icons;
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
          Icons::FaGithub.into(),
          "https://github.com/hiroaki-yamamoto",
          "Github",
        ),
        Link::new(
          Icons::FaGitlab.into(),
          "https://gitlab.com/hiroaki-yamamoto",
          "Gitlab",
        ),
        Link::new(
          Icons::FaKeybase.into(),
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
