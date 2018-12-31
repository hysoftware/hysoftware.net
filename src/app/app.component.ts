import { Component } from '@angular/core';

class Link {
  public icon: string | string[];
  public link: string;
  public name: string;
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.pug',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  protected misc: Link[] = [
    {
      icon: 'fas fa-file-pdf',
      link: '../assets/resume.pdf',
      name: 'Resume (PDF)'
    }
  ];
  protected snsList: Link[] = [
    {
      icon: 'fab fa-github',
      link: 'https://github.com/hiroaki-yamamoto',
      name: 'Github',
    },
    {
      icon: 'fab fa-gitlab',
      link: 'https://gitlab.com/hiroaki-yamamoto',
      name: 'Gitlab',
    },
    {
      icon: 'fab fa-linkedin',
      link: 'https://www.linkedin.com/in/hyamatan',
      name: 'Linkedin'
    },
    {
      icon: 'fab fa-angellist',
      link: 'https://angel.co/hiroaki-yamamoto',
      name: 'Angel List'
    },
    {
      icon: 'fab fa-keybase',
      link: 'https://keybase.io/hyamamoto',
      name: 'Keybase'
    }
  ];
}
