use ::std::sync::Arc;

use crate::icon::Icons;
use crate::links::Link;

#[derive(Debug)]
pub struct Ctrl {
  links: Vec<Arc<Link>>,
}

impl Ctrl {
  pub fn new() -> Self {
    Self {
      links: vec![
        Arc::new(Link::new(
          Icons::FaGithub.into(),
          "https://github.com/hiroaki-yamamoto",
          "_blank",
          "Github",
        )),
        Arc::new(Link::new(
          Icons::FaGitlab.into(),
          "https://gitlab.com/hiroaki-yamamoto",
          "_blank",
          "Gitlab",
        )),
        Arc::new(Link::new(
          Icons::FaKeybase.into(),
          "https://keybase.io/hyamamoto",
          "_blank",
          "Keybase",
        )),
      ],
    }
  }
  pub fn links(&self) -> &Vec<Arc<Link>> {
    return &self.links;
  }
}
