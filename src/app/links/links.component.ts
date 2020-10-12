import { Component, OnInit } from '@angular/core';
import { IconDefinition } from '@fortawesome/fontawesome-svg-core';
import { faFileCode } from '@fortawesome/free-solid-svg-icons';
import { faGithub, faGitlab, faLinkedin, faAngellist, faKeybase } from '@fortawesome/free-brands-svg-icons';

interface Link {
  icon: IconDefinition;
  link: string;
  name: string;
}

@Component({
  selector: 'app-links',
  styleUrls: ['./links.component.scss'],
  templateUrl: './links.component.html',
})
export class LinksComponent implements OnInit {

  public misc: Link[] = [
    {
      icon: faFileCode,
      link: 'https://github.com/hysoftware/hysoftware.net',
      name: 'Code of This Page'
    }
  ];
  public snsList: Link[] = [
    {
      icon: faGithub,
      link: 'https://github.com/hiroaki-yamamoto',
      name: 'Github',
    },
    {
      icon: faGitlab,
      link: 'https://gitlab.com/hiroaki-yamamoto',
      name: 'Gitlab',
    },
    {
      icon: faLinkedin,
      link: 'https://www.linkedin.com/in/hyamatan',
      name: 'Linkedin'
    },
    {
      icon: faAngellist,
      link: 'https://angel.co/hiroaki-yamamoto',
      name: 'Angel List'
    },
    {
      icon: faKeybase,
      link: 'https://keybase.io/hyamamoto',
      name: 'Keybase'
    }
  ];

  constructor() { }

  ngOnInit() {
  }

}
