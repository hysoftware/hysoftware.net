use ::std::string::ToString;

#[derive(Debug)]
pub struct Link {
  icon: Option<String>,
  href: String,
  text: String,
}

impl Link {
  pub fn new<T>(icon: Option<T>, href: &str, text: &str) -> Self
  where
    T: ToString,
  {
    return Self {
      icon: icon.map(|icon| icon.to_string()),
      href: href.into(),
      text: text.into(),
    };
  }
  pub fn icon(&self) -> &Option<String> {
    return &self.icon;
  }
  pub fn href(&self) -> &str {
    return &self.href;
  }
  pub fn text(&self) -> &str {
    return &self.text;
  }
}
